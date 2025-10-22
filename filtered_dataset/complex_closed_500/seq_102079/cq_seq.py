import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.09144, -0.09716).lineTo(-0.06604, -0.09716).lineTo(-0.06604, -0.11875).lineTo(-0.09144, -0.11875).lineTo(-0.09144, -0.09716).close()
solid=wp_sketch0.add(loop0).extrude(-0.051484184125956546)
