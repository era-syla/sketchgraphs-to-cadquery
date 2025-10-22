import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.02204, 0.05448).lineTo(0.02241, 0.05448).lineTo(0.02241, -0.0569).lineTo(-0.02204, -0.0569).lineTo(-0.02204, 0.05448).close()
solid=wp_sketch0.add(loop0).extrude(-0.10916008942013128)
