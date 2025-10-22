import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.07632, -0.03551).lineTo(0.07608, -0.03551).lineTo(0.07608, 0.09149).lineTo(-0.07632, 0.09149).lineTo(-0.07632, -0.03551).close()
solid=wp_sketch0.add(loop0).extrude(0.12878687673090344)
