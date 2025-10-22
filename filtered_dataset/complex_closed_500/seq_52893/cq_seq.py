import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.30099, 0.0019).lineTo(-0.30099, -0.00254).lineTo(-0.24511, -0.00254).lineTo(-0.24511, 0.00191).lineTo(-0.30099, 0.0019).close()
solid=wp_sketch0.add(loop0).extrude(0.1551617314917243)
