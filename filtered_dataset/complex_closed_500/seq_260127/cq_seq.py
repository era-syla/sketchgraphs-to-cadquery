import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.06, 0.0).lineTo(0.06, 0.07).lineTo(0.0, 0.07).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.12916531230344933)
