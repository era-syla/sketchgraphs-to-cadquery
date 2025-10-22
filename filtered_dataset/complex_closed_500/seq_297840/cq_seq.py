import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-1.28443, 2.85375).lineTo(-1.93246, 2.85375).lineTo(-1.93246, 0.0).lineTo(-1.28443, 0.0).lineTo(-1.28443, 2.85375).close()
solid=wp_sketch0.add(loop0).extrude(-6.33031687870476)
