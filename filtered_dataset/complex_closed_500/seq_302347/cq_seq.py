import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.02548, -0.02548).lineTo(-0.04326, -0.02548).lineTo(-0.04326, -0.04326).lineTo(-0.02548, -0.04326).lineTo(-0.02548, -0.02548).close()
solid=wp_sketch0.add(loop0).extrude(0.02516397789596858)
