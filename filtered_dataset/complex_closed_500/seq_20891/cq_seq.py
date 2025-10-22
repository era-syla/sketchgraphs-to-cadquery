import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.231, 0.05).lineTo(-0.231, 0.0).lineTo(-0.19092, 0.0).lineTo(-0.19092, 0.05).lineTo(-0.231, 0.05).close()
solid=wp_sketch0.add(loop0).extrude(-0.13440565267296917)
