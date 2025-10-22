import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.5903, 0.01295).lineTo(0.0193, 0.01295).lineTo(0.0193, 0.381).lineTo(0.5903, 0.381).lineTo(0.5903, 0.01295).close()
solid=wp_sketch0.add(loop0).extrude(1.592567506565829)
