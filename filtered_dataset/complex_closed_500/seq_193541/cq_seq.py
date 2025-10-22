import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(10.2675, 0.6).lineTo(10.8675, 0.6).lineTo(10.8675, 1.05).lineTo(10.2675, 1.05).lineTo(10.2675, 0.6).close()
solid=wp_sketch0.add(loop0).extrude(-0.7136970398756824)
