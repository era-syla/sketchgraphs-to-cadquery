import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.1335, -0.079).lineTo(-0.0198, -0.079).lineTo(-0.0198, -0.03161).lineTo(-0.1335, -0.03161).lineTo(-0.1335, -0.079).close()
solid=wp_sketch0.add(loop0).extrude(-0.03145461380084426)
