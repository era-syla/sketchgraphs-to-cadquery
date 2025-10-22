import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.06, 0.00025).lineTo(-0.06, 0.00525).threePointArc((-0.0625, 0.00275), (-0.06, 0.00025)).close()
solid=wp_sketch0.add(loop0).extrude(0.00659790493042913)
