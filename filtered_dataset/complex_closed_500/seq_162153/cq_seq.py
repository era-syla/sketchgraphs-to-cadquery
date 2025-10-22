import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0236, 0.006).lineTo(0.02528, 0.006).lineTo(0.02528, 0.01622).lineTo(-0.0236, 0.01622).lineTo(-0.0236, 0.006).close()
solid=wp_sketch0.add(loop0).extrude(-0.09742102004269762)
