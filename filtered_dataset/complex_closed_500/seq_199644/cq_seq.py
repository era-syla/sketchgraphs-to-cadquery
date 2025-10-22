import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.06109, 0.07736).lineTo(0.04051, 0.07736).lineTo(0.04051, 0.05831).lineTo(0.00241, 0.05831).lineTo(0.00241, 0.03291).lineTo(0.04051, 0.03291).lineTo(0.04051, 0.01386).lineTo(-0.06109, 0.01386).lineTo(-0.06109, 0.07736).close()
solid=wp_sketch0.add(loop0).extrude(-0.19486015102297663)
