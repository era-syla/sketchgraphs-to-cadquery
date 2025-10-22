import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.09872, -0.04832).lineTo(-0.11358, -0.04832).lineTo(-0.11358, 0.04542).lineTo(-0.09872, 0.04542).lineTo(-0.09872, -0.04832).close()
solid=wp_sketch0.add(loop0).extrude(0.21720496889072838)
