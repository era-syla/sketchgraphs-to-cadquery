import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.01584, 0.01542).lineTo(0.02196, 0.02333).lineTo(0.00219, 0.03863).lineTo(-0.00393, 0.03072).lineTo(0.01584, 0.01542).close()
solid=wp_sketch0.add(loop0).extrude(0.07251122462387218)
