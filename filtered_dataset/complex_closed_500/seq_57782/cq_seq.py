import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.07557, -0.03785).lineTo(-0.07557, -0.03785).lineTo(-0.07557, 0.03785).lineTo(0.07557, 0.03785).lineTo(0.07557, -0.03785).close()
solid=wp_sketch0.add(loop0).extrude(-0.27005370859585254)
