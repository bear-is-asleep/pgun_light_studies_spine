## Particle Gun Studies
These studies look at the light at varying degrees of truth (g4, reconstructed flash, hypothesis flash) with respect to the associated depositions (g4, truth, reco).

## How to Run
0. Produce larcv and opana files using the [LArSoft repo](https://github.com/bear-is-asleep/pgun_light_studies)
1. Copy files in following structure `study_name/opana` has all `opana*.root` files. `study_name/larcv` has all of the `larcv*.root` files. These can be safely hadded together, since the particle gun configuration is saved in `simulation_log.csv`.
2. Run the inference and reconstruction using [spine_prod](https://github.com/DeepLearnPhysics/spine_prod/) (`latest.cfg` should do)
3. Now you can run flash matching using one of the configs in the repo using `spine_prod` again. This time a folder called `study_name/logs` will be made. After it's done running, rename it according to the following table

| File Name            | Log Type     |
|----------------------|--------------|
| `fmatch.cfg`        | `reco_logs`  |
| `fmatch_truth.cfg`  | `truth_logs` |
| `fmatch_g4.cfg`     | `g4_logs`    |

4. Once you've done all of this, you can run `python combine_logs.py` to combine the logs into single csvs
5. Now you can run the notebook! Good luck!
