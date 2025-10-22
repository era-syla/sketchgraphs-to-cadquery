import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.57785, 0.57785).lineTo(-0.57785, 0.57785).lineTo(-0.57785, -0.57785).lineTo(0.57785, -0.57785).lineTo(0.57785, 0.57785).close()
solid=wp_sketch0.add(loop0).extrude(1.2681373996315717)
