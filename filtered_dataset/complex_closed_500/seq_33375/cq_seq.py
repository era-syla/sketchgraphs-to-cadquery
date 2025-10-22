import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.02599, 0.011).lineTo(-0.03019, 0.011).lineTo(-0.03019, 0.0072).lineTo(-0.02599, 0.0072).lineTo(-0.02599, 0.011).close()
solid=wp_sketch0.add(loop0).extrude(0.006313774945326136)
