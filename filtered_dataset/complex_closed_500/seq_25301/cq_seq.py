import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0188, -0.05931).lineTo(0.0128, -0.05931).threePointArc((0.0158, -0.06231), (0.0188, -0.05931)).close()
solid=wp_sketch0.add(loop0).extrude(0.012498132444150017)
