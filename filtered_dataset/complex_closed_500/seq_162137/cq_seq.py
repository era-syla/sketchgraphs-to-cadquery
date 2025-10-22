import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.21749, -0.03651).lineTo(0.21749, -0.03651).lineTo(0.21749, -0.03493).lineTo(-0.21749, -0.03493).lineTo(-0.21749, -0.03651).close()
solid=wp_sketch0.add(loop0).extrude(0.8117258765387081)
