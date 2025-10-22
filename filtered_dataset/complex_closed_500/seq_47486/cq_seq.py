import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.045, 0.0).lineTo(-0.045, 0.08).lineTo(-0.055, 0.08).lineTo(-0.055, 0.06925).threePointArc((-0.05273, 0.06062), (-0.05471, 0.05191)).lineTo(-0.057, 0.04733).lineTo(-0.057, 0.01988).lineTo(-0.057, 0.0).lineTo(-0.045, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.1393228630276364)
