import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0005, 0.03076).lineTo(0.0095, 0.03076).lineTo(0.0095, 0.04076).lineTo(-0.0005, 0.04076).lineTo(-0.0005, 0.03076).close()
solid=wp_sketch0.add(loop0).extrude(-0.015203740936986976)
