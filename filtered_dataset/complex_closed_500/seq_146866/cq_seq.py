import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.01626, -0.01627).lineTo(0.01738, -0.01627).lineTo(0.01738, 0.00258).lineTo(-0.01626, 0.00258).lineTo(-0.01626, -0.01627).close()
solid=wp_sketch0.add(loop0).extrude(-0.09485403402581966)
