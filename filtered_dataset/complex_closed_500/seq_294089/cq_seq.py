import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.01213, 0.111).lineTo(0.01327, 0.111).lineTo(0.01327, 0.10719).lineTo(-0.01213, 0.10719).lineTo(-0.01213, 0.111).close()
solid=wp_sketch0.add(loop0).extrude(0.010999798972069862)
