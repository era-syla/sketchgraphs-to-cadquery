import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.00279, 0.00477).lineTo(-0.00321, 0.00477).lineTo(-0.00321, -0.00923).lineTo(0.00279, -0.00923).lineTo(0.00279, 0.00477).close()
solid=wp_sketch0.add(loop0).extrude(0.013614336735885003)
