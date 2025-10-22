import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.005, -0.04075).lineTo(0.005, -0.04075).lineTo(0.005, -0.03375).lineTo(-0.005, -0.03375).lineTo(-0.005, -0.04075).close()
solid=wp_sketch0.add(loop0).extrude(0.020134611726448818)
