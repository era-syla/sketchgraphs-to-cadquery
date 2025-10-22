import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-3.2, -0.65).lineTo(-2.1825, -0.65).lineTo(-2.1825, 0.4).lineTo(-3.2, 0.4).lineTo(-3.2, -0.65).close()
solid=wp_sketch0.add(loop0).extrude(0.5397022573396407)
