# WASP Cloud Computing Course Assignment

This is a small project for the WASP cloud computing course where matrix
computations on a Apache Spark cluster in the Google DataProc cloud is
evaluated.

## Project Notes

- Don't waste time trying to install Apache Spark. It is already installed and
  available on a Google DataProc cluster, so create one of those instead of
  trying to use other clusters.

- Add a public SSH key to the cluster to get access to a proper shell. Don't
  bother with *OS Login*, simply add a key to the instance meta data. Go to:

  - Compute Engine -> Metadata -> SSH Keys -> Edit -> Add Item.

  - To use the spark instance, you need the external IP of the DataProc master
    node. It can be found here: Compute Engine -> VM Instances -> External IP.

  - Add an entry to your `~/.ssh/config` for easy login to the master node:

    ```
    host google-cloud
      ForwardX11 no
      User <Username>
      HostName <External-IP>
      IdentityFile <Private-SSH-Key>
    ```

- It is a good idea to pin the Compute Engine, Dataproc and Storage menu items,
  since you will likely refer to them quite a bit.

- Either rename the default bucket name, or export a shell variable with the
  name to save yourself quite a bit of typing.

- I recommend following the Googles' Apache Spark
  [tutorial](https://cloud.google.com/dataproc/docs/tutorials/gcs-connector-spark-tutorial)
  as it contains a bit more information about how to *actually* create HDFS
  datasets, refer to them and use them in scripts, etc.

- Oddly enough, `scipy.io.mmread()` appears to be `python2` only. Should
  probably report that as a bug at some point.

- SparseQR cannot handle matrices at 100000x100000 or larger (runs out of
  memory).

- When saving/restoring a RDD, I recommend using `saveAsPickleFile()` and
  `pickleFile()` in order to avoid having to parse a RDD textfile in order to
  restore the RDD.

- If you're missing Python packages, login to the Spark master node and use
  `apt` to install the packages. E.g., `sudo apt install python-scipy` for the
  python2.7 version of SciPy.
