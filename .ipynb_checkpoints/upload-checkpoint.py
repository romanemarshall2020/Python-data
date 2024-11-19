import json

with open('./archive/dataset/cpu.json', 'r') as f:
    cpu_json_data = f.read()

cpu_dict = json.loads(cpu_json_data)
cpu_dict_prettier = json.dumps(cpu_dict, indent=1)
# print(cpu_dict_prettier)
def filter_by_brand(cpu_catalog):
    filter_list = []
    remaining_items = []
    search_str = input("please enter an input: ")
    print(len(cpu_catalog))
    for dict in cpu_catalog:
        # is_name = dict["name"].__contains__(search_str)
        if search_str in dict["name"]:
            filter_list.append(dict)
        else:
            remaining_items.append(dict)

        # clean_list = json.dumps(filter_list, indent=1)    

        # print(clean_list)
    return filter_list

# filter(cpu_dict)


results = filter_by_brand(cpu_dict)
isgpu_list = []
nogpu_list = []
def filter_by_graphics(dictionary):
    for gpu in dictionary: 
        gpu_status = gpu.get("graphics")
        if gpu_status is not None:
            isgpu_list.append(gpu)
        else:
            nogpu_list.append(gpu)

        clean_gpu_list = json.dumps(isgpu_list, indent=1)    

        print(clean_gpu_list)



filter_by_graphics(results)




# # this function must sort cpu's by some sort of sort order
# def sort_catalog(cataloge: list[dict], sort_by: str, direction_ascending: bool) -> list[dict]:
#     sorted_list = cataloge.sorted()
#     print (sorted_list)

    



#     # boolean
#     # list[{}]