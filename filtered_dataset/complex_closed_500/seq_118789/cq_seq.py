import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.005, -0.0675).lineTo(0.005, -0.074).lineTo(0.008, -0.074).lineTo(0.008, -0.061).lineTo(0.005, -0.061).lineTo(0.005, -0.0675).close()
solid=wp_sketch0.add(loop0).extrude(-0.003305990969784128)
