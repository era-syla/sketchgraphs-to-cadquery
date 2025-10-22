import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.31838, -0.23035).lineTo(-0.13423, -0.23035).lineTo(-0.13423, -0.0462).lineTo(-0.31838, -0.0462).lineTo(-0.31838, -0.23035).close()
solid=wp_sketch0.add(loop0).extrude(-0.008237812139293798)
