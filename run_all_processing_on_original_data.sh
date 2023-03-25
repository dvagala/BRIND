
rm -rf test_gt test_imgs train_gt train_imgs tmp_data

cp -r original_data tmp_data


python3 treshold_edges.py tmp_data/ground_truth_images
echo "tresholding edges done"

python3 split_into_train_and_test.py
echo "spliting into train and test done"

python3 augment_train_data.py 20
echo "augmenting train data done"

python3 generate_lst_file_for_ldc.py
echo "generating list file done"


rm -rf tmp_data