import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.03061, 0.02081).lineTo(-0.02331, 0.02081).lineTo(-0.02331, 0.00581).lineTo(-0.03061, 0.00581).lineTo(-0.03061, 0.02081).close()
solid=wp_sketch0.add(loop0).extrude(-0.03351813696323803)
