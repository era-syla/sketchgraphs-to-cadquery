import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0127, 0.0127).lineTo(0.0635, 0.0127).lineTo(0.0635, 0.03175).lineTo(0.0127, 0.03175).lineTo(0.0127, 0.0127).close()
solid=wp_sketch0.add(loop0).extrude(-0.03009843392459871)
