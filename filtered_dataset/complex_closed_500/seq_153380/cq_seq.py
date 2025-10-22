import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0045, 0.032).lineTo(-0.0115, 0.032).lineTo(-0.0115, 0.022).lineTo(-0.0045, 0.022).lineTo(-0.0045, 0.032).close()
solid=wp_sketch0.add(loop0).extrude(-0.0027549756562920895)
