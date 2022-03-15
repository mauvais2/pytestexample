import numpy as np
import deepchem as dc

def test_split():
    N_samples = 50
    n_features = 10
    X = np.random.rand(N_samples, n_features)
    y = np.random.rand(N_samples)
    dataset = dc.data.NumpyDataset(X, y)

    dataset = dc.data.NumpyDataset(X, y)
    dataset.X.shape
    dataset.y.shape

    properties = [0.4, -1.5, 3.2, -0.2, 1.7]
    featurizer = dc.feat.CircularFingerprint(size=1024)
    ecfp = featurizer.featurize(smiles)
    ecfp.shape

    dataset = dc.data.NumpyDataset(X=ecfp, y=np.array(properties))
    assert len(dataset) == 5

    splitter = dc.splits.RandomSplitter()
    train_dataset, valid_dataset, test_dataset = splitter.train_valid_test_split(dataset=dataset, frac_train=0.6, frac_valid=0.2, frac_test=0.2)

    assert len(train_dataset) == 3
    assert len(valid_dataset) == 1
    assert len(test_dataset) == 1
