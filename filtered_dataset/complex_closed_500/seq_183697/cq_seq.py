import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.13569, 0.02893).lineTo(0.27069, 0.02893).lineTo(0.27069, -0.01607).lineTo(0.13569, -0.01607).lineTo(0.13569, 0.02893).close()
solid=wp_sketch0.add(loop0).extrude(-0.23820020050340762)
