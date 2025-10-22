import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.02929, 0.02341).lineTo(-0.03979, 0.02341).lineTo(-0.03979, 0.01241).lineTo(-0.02929, 0.01241).lineTo(-0.02929, 0.02341).close()
solid=wp_sketch0.add(loop0).extrude(-0.019789929912415172)
