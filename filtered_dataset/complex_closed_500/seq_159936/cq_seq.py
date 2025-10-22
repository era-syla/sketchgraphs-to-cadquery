import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-1.49066, 2.3368).lineTo(-1.49066, 1.8034).lineTo(-0.54769, 1.8034).lineTo(-0.54769, 0.0).lineTo(-0.52864, 0.0).lineTo(-0.52864, 2.3368).lineTo(-1.49066, 2.3368).close()
solid=wp_sketch0.add(loop0).extrude(3.609202877620196)
