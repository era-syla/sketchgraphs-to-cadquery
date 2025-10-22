import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.00254, 0.0).lineTo(-0.00254, -0.00508).threePointArc((-0.00508, -0.00254), (-0.00254, 0.0)).close()
solid=wp_sketch0.add(loop0).extrude(0.005160141951343298)
