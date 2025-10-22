import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.07303, -0.07325).lineTo(-0.0718, -0.07325).lineTo(-0.0718, 0.06905).lineTo(0.07303, 0.06905).lineTo(0.07303, -0.07325).close()
solid=wp_sketch0.add(loop0).extrude(-0.07335721092640024)
