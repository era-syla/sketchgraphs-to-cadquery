import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.4572, -0.0472).lineTo(-0.3556, -0.0472).lineTo(-0.3556, -0.05355).lineTo(-0.4572, -0.05355).lineTo(-0.4572, -0.0472).close()
solid=wp_sketch0.add(loop0).extrude(-0.03821519931072268)
