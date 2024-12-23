import AugmentationClass as aug

#tworzenie zbiory danych dwu wymiarowych x_train oraz y_train za pomocą funkcji make_blobs z sklearn.datasets.
#Jest w tym zbiorze danych 300 punktów otoczonych wokół jednego centrum, które zostały stworzone w oparciu o jedno odchylenie standardowe
x_train, y_train = make_blobs(n_samples=500, centers=1, random_state=42, cluster_std=1.0)

#pokazywanie że w x_train znajdują się dwie kolumny o liczbie wierszy 300
print(pd.DataFrame(x_train).shape)

#skalowanie danych Standardowym skalowaniem z biblioteki sklearn.preprocesing
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)

#aplikowanie metody LOF
x_train = remove_outliers_lof(x_train)

print(len(x_train))

#szukanie środka ciężkości całego wykresu, aby móc przesunąć go na środek by późniejsza augmentacja stała się łatwiejsza z punktem zaczepienia wektorów
#wokół punktu (0,0) w dwu wymiarowej przestrzeni.
df = pd.DataFrame(x_train, columns=['x', 'y'])
mean_x = df['x'].mean()
mean_y = df['y'].mean()

new_point = [mean_x, mean_y]

#przesuwanie danych o środek ciężkości aby on był na środku układu współrzędnych
x_train = x_train - [mean_x, mean_y]

#sprowadzanie wartosci do tabeli pandas
x = pd.DataFrame(longest_distance(x_train))
print(x.head())

#sortowanie
x.sort_values(by=[0], ascending=False, inplace=True)
len_list = x.values.tolist()

print(len_list[:5])

#rozpietosc wykresu - sprawdzanie
coord_max = x.max()
coord_min = x.min()
coord_max = coord_max.values.tolist()
coord_min = coord_min.values.tolist()
coord_max.pop(0)
coord_min.pop(0)

print(len(len_list))

x_dist = abs(coord_max[0]) + abs(coord_min[0])
y_dist = abs(coord_max[1]) + abs(coord_min[1])

n_angles =5

angle_of_rotation = 2*np.pi/n_angles

x = len_list[0][1]
y = len_list[0][2]

V = [x,y]

V[0] = math.cos(angle_of_rotation/2)*x - math.sin(angle_of_rotation/2)*y
V[1] = math.sin(angle_of_rotation/2)*x + math.cos(angle_of_rotation/2)*y

Vx = math.cos(angle_of_rotation*n_angles)*V[0] - math.sin(angle_of_rotation*n_angles)*V[1]
Vy = math.sin(angle_of_rotation*n_angles)*V[0] + math.cos(angle_of_rotation*n_angles)*V[1]

print(len_list[0])

edge_points = [len_list[0]]

print(edge_points)

base_vector = [Vx, Vy]
base_vector = np.array(base_vector)

sections = [[] for _ in range(n_angles)]

count = 0
for i in range(len(len_list)):
    vector_point = [len_list[i][1], len_list[i][2]]
    vector_point = np.array(vector_point)
    for j in range(0,n_angles):
        angle_comp_base_vector = angle_vector_point(base_vector, vector_point)

        if angle_of_rotation*j < angle_comp_base_vector < angle_of_rotation*(j+1):
            sections[j].append(vector_point)
            count += 1
            break

print(count)

print(sections[0][0])

angle_rad = []

start_angle = np.arctan(y/x)

V[0] = math.cos(angle_of_rotation/2)*x - math.sin(angle_of_rotation/2)*y
V[1] = math.sin(angle_of_rotation/2)*x + math.cos(angle_of_rotation/2)*y

for i in range(n_angles):
  angle_rad.append(np.arctan(y/x) + 3/2*angle_of_rotation*i)

angle_rad = np.array(angle_rad)

sections = [[sections[j][i].tolist() for i in range(len(sections[j]))] for j in range(len(sections))]

print(angle_rad)

for i in range(n_angles):
    print(sections[i][0], euclidean_distance(sections[i][0][0], sections[i][0][1]))

print(edge_points)
print(angle_rad)

edge_points = []
for edge in range(n_angles):
    edge_points.append(sections[edge][0])

print(edge_points)

print(sections[0][0])

plt.figure(figsize=(10,10))

colors = [
    'orange', 'green', 'purple',
    'brown', 'pink', 'gray']

color_iterator = 0

for i in range(n_angles):
    if color_iterator >= len(colors) - 1:
        color_iterator = 0
    section_array = np.array(sections[i])
    plt.scatter(section_array[1:, 0], section_array[1:, 1], color=colors[color_iterator], alpha=0.5, s=10)
    color_iterator += 1

angle_rad = []
if y > 0:
    start_angle = np.arctan(y/x)
else:
    start_angle = np.pi + np.arctan(y/x)

print(start_angle)


V[0] = math.cos(angle_of_rotation/2)*x - math.sin(angle_of_rotation/2)*y
V[1] = math.sin(angle_of_rotation/2)*x + math.cos(angle_of_rotation/2)*y

for i in range(n_angles):

  Vx = math.cos(angle_of_rotation*i)*V[0] - math.sin(angle_of_rotation*i)*V[1]
  Vy = math.sin(angle_of_rotation*i)*V[0] + math.cos(angle_of_rotation*i)*V[1]

  plt.quiver(0, 0, Vx, Vy, angles='xy', scale_units='xy', scale=1, color='red', width=0.003)

edge_points = []

for edge in range(n_angles):
    edge_points.append(sections[edge][0])

edge_points = np.array(edge_points)

for i in range(len(edge_points)):
    if color_iterator > len(colors) - 1:
        color_iterator = 0

    plt.scatter(edge_points[i:, 0], edge_points[i:, 1], color=colors[color_iterator], alpha=0.9, s=20)
    color_iterator += 1

first_angle = start_angle - angle_of_rotation/2

#wycinek kola
for i in range(n_angles):
    wycinek_edge = Wedge(center=(0, 0), r=euclidean_distance(edge_points[i][0],edge_points[i][1]), theta1=np.degrees(first_angle + angle_of_rotation*(i+1)), theta2=np.degrees(first_angle + angle_of_rotation*(i+2)), width=0.001, color='black')
    if first_angle + angle_of_rotation*(i+1) <= 2*np.pi:
        angle_rad.append(first_angle + angle_of_rotation*(i+1))
    else:
        angle_rad.append((first_angle + angle_of_rotation*(i+1)) - 2*np.pi)
    plt.gca().add_patch(wycinek_edge)

angle_rad.append(angle_rad[0])

plt.xlim(-3.5, 3.5)
plt.ylim(-3.5, 3.5)

plt.gca().set_aspect('equal')

plt.xlabel("x")
plt.ylabel("y")
plt.title("blobs")
plt.show()

sections_len = [len(sections[i]) for i in range(len(sections))]
data_len = sum(sections_len)

sections_occur_percentage = [sections_len[i]/data_len for i in range(len(sections))]

subsections_number = [4*math.ceil(sections_occur_percentage[i])+1 for i in range(n_angles)]

print(subsections_number)

equal_radiouses = radious_of_equal_areas(3,5)

print(equal_radiouses)

print(angle_rad)

subsection_angle = [angle_of_rotation/(subsections_number[i]) for i in range(n_angles)]

print(subsection_angle)

#subsekcje - [i][j][k] -> i - numer sekcji, j,k -> numer podsekcji w danej sekcji w zaleznosci od kąta(j) oraz promienia(k), l -> [x, y] w tablicy

subsections = [ [ [ [] for areas in range(subsections_number[sect_num])] for sub_sect in range(subsections_number[sect_num]) ] for sect_num in range(len(sections)) ]

print(len(subsections[0][0]))

print(sections[1][1])

print(is_in_angle(-1,-2,3.888696759489716, 4.786294660515371))

if is_in_angle(-1,-2,3.888696759489716, 4.786294660515371):
    print("true")

print(len(subsections[:]))

# distance_from_center = euclidean_distance(sections[i][j][0],sections[i][j][1])
# equal_radiouses = radious_of_equal_areas(edge_points[i],subsections_number[i])
# is_in_angle_result = is_in_angle(sections[i][j][0], sections[i][j][1], angle_rad[k]+subsection_angle*k, angle_rad[k]+subsection_angle*(k+1))

ctrl_sum = 0
ctrl_tab = []
for sect in range(len(sections)):

    equal_radiouses = radious_of_equal_areas(euclidean_distance(edge_points[sect][0],edge_points[sect][1]),subsections_number[sect])

    for pts in range(len(sections[sect])):


        for i in range(subsections_number[sect]):

            is_in_angle_result = is_in_angle(sections[sect][pts][0],sections[sect][pts][1], angle_rad[sect] + subsection_angle[sect]*i, angle_rad[sect] + subsection_angle[sect]*(i+1))


            if is_in_angle_result:

                distance_from_center = euclidean_distance(sections[sect][pts][0],sections[sect][pts][1])


                for j in range(subsections_number[sect]):

                    if equal_radiouses[j] < distance_from_center and distance_from_center <= equal_radiouses[j+1]:

                        subsections[sect][i][j].append(sections[sect][pts])
                        ctrl_tab.append(sections[sect][pts])
                        ctrl_sum += 1
                        break

print(ctrl_sum)
s = 0
#284 - 270 dla 300 pkt
#485 - 465 dla 500 pkt
for sect in range(len(sections)):
    s += len(sections[sect])
print(s)

print(len(subsections[0][4][1]))

for i in range(len(subsections)):
    for j in range(len(subsections[i])):
        for k in range(len(subsections[i][j])):
            if len(subsections[i][j][k]) == 0:
                print(i,j,k)

print(len(subsections[0][4][4]))

count_of_elem = [ [ [] for j in range(len(subsections[i]))] for i in range(len(subsections))]

c = 0
for i in range(len(subsections)):
    for j in range(len(subsections[i])):
        for k in range(len(subsections[i][j])):
            c += 1
            count_of_elem[i][j].append(len(subsections[i][j][k]))

print(c)

print(len(count_of_elem) * len(count_of_elem[0]) * len(count_of_elem[0][0]))

print(count_of_elem[0][0][0])

print(sum(count_of_elem[0][0]))

print(subsections[0][0][4])

perc_of_occ = [ [ [] for j in range(len(subsections[i]))] for i in range(len(subsections))]

for i in range(len(subsections)):
    for j in range(len(subsections[i])):
        for k in range(len(subsections[i][j])):
            if sum(count_of_elem[i][j]) != 0:
                perc_of_occ[i][j].append(count_of_elem[i][j][k]/sum(count_of_elem[i][j]))
            else:
                perc_of_occ[i][j].append(0.01)

print(perc_of_occ[0][0])

sum = 0
for i in range(len(subsections)):
    for j in range(len(subsections[i])):
        for k in range(len(subsections[i][j])):
            for l in range(len(subsections[i][j][k])):
                sum += 1
print(sum)

print(subsections[0][0][2][2][0])

print(len(ctrl_tab))

print(len(x_train))

difference_list = compare_points(x_train,ctrl_tab)

print(difference_list)

for i in range(len(difference_list)):
    difference_list[i] = np.array(difference_list[i])

difference_list = np.array(difference_list)

plt.figure(figsize=(5, 5))
plt.scatter(difference_list[:, 0], difference_list[:, 1], color='red', s=20)
plt.xlim(-3.5, 3.5)
plt.ylim(-3.5, 3.5)

plt.gca().set_aspect('equal')

plt.xlabel("x")
plt.ylabel("y")
plt.title("blobs")
plt.show()

c = 0
for i in range(len(difference_list)):
    if is_in_angle(difference_list[i][0],difference_list[i][1],0,subsection_angle[0]):
        c += 1

subsections_test = [ [ [ [] for areas in range(subsections_number[sect_num])] for sub_sect in range(subsections_number[sect_num]) ] for sect_num in range(len(sections)) ]

len(x_train)

ctrl_sum_test = 0
ctrl_tab_test = []
for sect in range(n_angles):

    equal_radiouses = radious_of_equal_areas(euclidean_distance(edge_points[sect][0],edge_points[sect][1]),subsections_number[sect])

    for pts in range(len(x_train)):


        for i in range(subsections_number[sect]):

            subangle_start = angle_rad[sect] + subsection_angle[sect]*i
            subangle_end = angle_rad[sect] + subsection_angle[sect]*(i+1)


            is_in_angle_result = is_in_angle(x_train[pts][0],x_train[pts][1], subangle_start, subangle_end)


            if is_in_angle_result:

                distance_from_center = euclidean_distance(x_train[pts][0],x_train[pts][1])


                for j in range(subsections_number[sect]):

                    if equal_radiouses[j] < distance_from_center <= equal_radiouses[j+1]:

                        subsections[sect][i][j].append(x_train[pts])
                        ctrl_tab_test.append(x_train[pts])
                        ctrl_sum_test += 1
                        break

print(len(ctrl_tab_test))

[random.uniform(0,2) for i in range(10)]

