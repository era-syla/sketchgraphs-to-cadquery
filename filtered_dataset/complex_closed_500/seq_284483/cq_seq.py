import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.02075, -0.01754).lineTo(-0.02075, -0.01754).lineTo(-0.02075, -0.06009).lineTo(0.02075, -0.06009).lineTo(0.02075, -0.01754).close()
solid=wp_sketch0.add(loop0).extrude(0.08886871700313186)
