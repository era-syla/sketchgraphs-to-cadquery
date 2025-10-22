import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0125, -0.017).lineTo(0.0125, -0.017).lineTo(0.0125, 0.013).lineTo(-0.0125, 0.013).lineTo(-0.0125, -0.017).close()
solid=wp_sketch0.add(loop0).extrude(-0.02555345511398646)
