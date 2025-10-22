import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.06794, 0.0685).lineTo(0.05937, 0.0685).lineTo(0.05937, -0.04534).lineTo(-0.06794, -0.04534).lineTo(-0.06794, 0.0685).close()
solid=wp_sketch0.add(loop0).extrude(-0.02741179896436885)
