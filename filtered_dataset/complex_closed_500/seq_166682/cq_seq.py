import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.04825, 0.01).lineTo(0.05825, 0.01).lineTo(0.05825, -0.01).lineTo(0.04825, -0.01).lineTo(0.04825, 0.01).close()
solid=wp_sketch0.add(loop0).extrude(0.005192815991412072)
