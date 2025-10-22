import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0231, -0.0).lineTo(0.0241, -0.0).lineTo(0.0241, 0.0185).lineTo(0.0231, 0.0185).lineTo(0.0231, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.0018746792796560155)
