import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0444, 0.04146).lineTo(0.04115, 0.04146).lineTo(0.04115, -0.04819).lineTo(-0.0444, -0.04819).lineTo(-0.0444, 0.04146).close()
solid=wp_sketch0.add(loop0).extrude(0.026866459037542006)
