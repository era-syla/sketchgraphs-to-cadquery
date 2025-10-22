import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.13442, 0.01996).lineTo(-0.1282, 0.01996).lineTo(-0.1282, 0.01852).lineTo(-0.13442, 0.01852).lineTo(-0.13442, 0.01996).close()
solid=wp_sketch0.add(loop0).extrude(-0.0057144812038448746)
