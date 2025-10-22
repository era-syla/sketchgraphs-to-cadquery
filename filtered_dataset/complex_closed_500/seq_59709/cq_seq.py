import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.09461, -0.0179).lineTo(-0.05609, -0.0179).lineTo(-0.05609, -0.06096).lineTo(-0.09461, -0.06096).lineTo(-0.09461, -0.0179).close()
solid=wp_sketch0.add(loop0).extrude(-0.030142424337877526)
