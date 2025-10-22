import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.01322, -0.00364).lineTo(0.01594, -0.00364).lineTo(0.01594, -0.02207).lineTo(0.01322, -0.02207).lineTo(0.01322, -0.00364).close()
solid=wp_sketch0.add(loop0).extrude(0.039950727358281805)
